def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[5:10].lower()
    filtered_letters = [c for c in s_lower if c in english_letters]
    palindromes = set()
    for i in range(len(filtered_letters)):
        for j in range(i + 1, len(filtered_letters)):
            for k in range(j + 1, len(filtered_letters)):
                triplet = [filtered_letters[i], filtered_letters[j], filtered_letters[k]]
                for perm in permutations(triplet):
                    word = ''.join(perm)
                    if is_palindrome(word):
                        palindromes.add(word)
    return palindromes