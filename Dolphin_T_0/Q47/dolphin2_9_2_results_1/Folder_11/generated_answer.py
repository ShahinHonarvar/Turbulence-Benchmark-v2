def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[24:98]
    for i in range(len(substring)):
        for j in range(i + 9, len(substring) + 1):
            sub = substring[i:j]
            if len(sub) in range(10, 37) and sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result