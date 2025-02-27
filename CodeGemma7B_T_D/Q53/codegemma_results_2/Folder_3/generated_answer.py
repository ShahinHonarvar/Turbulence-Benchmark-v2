def palindrome_of_length_at_least_n(str):
    final = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            sliced = str[i:j + 1]
            if sliced == sliced[::-1] and len(sliced) >= 59 and sliced.isalpha():
                final.add(sliced)
    return final