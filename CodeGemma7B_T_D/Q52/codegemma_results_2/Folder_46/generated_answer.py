def palindrome_of_length_n(str):
    palindrome_set = set()
    str = str.lower()
    for i in range(len(str) - 463):
        for j in range(i + 464):
            substring = str[i:j]
            half_length = len(substring) // 2
            for k in range(half_length):
                if substring[k] != substring[len(substring) - k - 1]:
                    break
            else:
                palindrome_set.add(substring)
    return palindrome_set