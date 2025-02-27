def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[118:257].lower()
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes