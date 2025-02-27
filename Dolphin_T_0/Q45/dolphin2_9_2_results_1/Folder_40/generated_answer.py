def palindromes_between_indices(s):
    substring = ''
    for i in range(4, 10):
        substring += s[i].lower()
    palindromes = set()
    for p in range(len(substring)):
        for q in range(p + 7, len(substring) + 1):
            substring_for_check = substring[p:q]
            if substring_for_check == substring_for_check[::-1]:
                palindromes.add(substring_for_check)
    return palindromes