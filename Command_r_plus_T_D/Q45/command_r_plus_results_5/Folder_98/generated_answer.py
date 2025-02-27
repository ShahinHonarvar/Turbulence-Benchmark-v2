def palindromes_between_indices(s):
    s = s.lower()
    sub_str = s[3:6]
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 4, len(sub_str) + 1):
            temp_str = sub_str[i:j]
            if temp_str == temp_str[::-1]:
                palindromes.add(temp_str)
    return palindromes