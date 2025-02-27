def palindrome_of_length_at_least_n(str):
    str = str.lower()
    result = set()
    for i in range(len(str)):
        for j in range(i + 1, min(len(str), i + 24)):
            if str[i:j] == str[j - 1:i:-1]:
                result.add(str[i:j])
    return result