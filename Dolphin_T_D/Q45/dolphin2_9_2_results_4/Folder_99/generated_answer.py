def palindromes_between_indices(s):
    substring = s[4:9]
    substring_set = set(substring)
    palindrome_set = set()
    for length in range(3, len(substring) + 1):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            sub_set = set(sub.lower())
            if sub_set == substring_set and sub == sub[::-1]:
                palindrome_set.add(sub)
    return palindrome_set