def palindromes_between_indices(s):
    set_of_all_palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if len(substring) >= 4 and substring == substring[::-1]:
                set_of_all_palindromes.add(substring.lower())
    return set_of_all_palindromes