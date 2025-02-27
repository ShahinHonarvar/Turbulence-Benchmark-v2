def palindromes_of_specific_lengths(str):
    str = str.lower()
    result = set()
    for i in range(len(str)):
        for j in range(i + 3, 5):
            if str[i:j + 1] == str[i:j + 1][::-1]:
                result.add(str[i:j + 1])
    return result