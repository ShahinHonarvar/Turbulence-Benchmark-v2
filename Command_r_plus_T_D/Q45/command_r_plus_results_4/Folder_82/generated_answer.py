def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_between_indices = set(s[1:7].lower())
    if not letters_between_indices.issubset(english_letters):
        return set()
    all_palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, 8):
            for perm in permutations(s[1:7], i):
                for perm_j in permutations(s[1:7], j):
                    palindrome = ''.join(perm + perm_j[::-1])
                    if is_palindrome(palindrome):
                        all_palindromes.add(palindrome)
    return all_palindromes