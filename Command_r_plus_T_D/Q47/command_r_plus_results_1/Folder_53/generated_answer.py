def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[1:300].lower()
    for length in range(3, 11):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes