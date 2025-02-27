def palindromes_of_specific_lengths(s):
    s = s.lower()
    found_palindromes = set()
    substring = s[2:9]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            part = ''.join(filter(str.isalpha, substring[i:j]))
            if part == part[::-1]:
                found_palindromes.add(part)
    return found_palindromes