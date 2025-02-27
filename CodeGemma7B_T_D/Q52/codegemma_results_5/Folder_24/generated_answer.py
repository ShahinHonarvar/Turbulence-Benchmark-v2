def palindrome_of_length_n(text: str) -> set[str]:
    """
                Checks text for palindromes of length n and returns set of matches or an empty set if none found.
            """
    all_polindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                all_polindromes.add(substring.lower())
    return all_polindromes