def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[127:289]
    palindromes = set()
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i + length]
            if all((ch.isalpha() for ch in substring_part)) and substring_part == substring_part[::-1]:
                palindromes.add(substring_part)
    return palindromes