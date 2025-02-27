def palindromes_of_specific_lengths(s: str) -> set:
    substr = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if all((letter.isalpha() for letter in sub)) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes