def palindromes_between_indices(text: str) -> set[str]:

    def find(text: str, start: int, end: int) -> set[str]:
        if end - start < 6:
            return set()
        unique_letters = set(text[start:end])
        if len(unique_letters) < 7:
            return set()
        unique_letters = sorted(unique_letters)
        palindromes = set()
        for permutation in itertools.permutations(unique_letters):
            palindrome = ''.join(permutation) * ((end - start) // 7)
            if palindrome.endswith(text[start:end]):
                palindromes.add(palindrome)
        return palindromes
    text = text.lower()
    if not text[1:9].isalpha():
        return set()
    return find(text, 1, 9)