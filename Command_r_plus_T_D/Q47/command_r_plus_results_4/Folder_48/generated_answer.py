def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[154:284].lower()
    palindromes = set()
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes