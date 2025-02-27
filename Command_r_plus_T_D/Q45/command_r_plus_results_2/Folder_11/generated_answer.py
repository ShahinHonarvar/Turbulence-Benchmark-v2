def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = [char for char in s[3:8] if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters)):
            for k in range(j + 1, len(english_letters)):
                triplet = english_letters[i:k + 1]
                for word in [''.join(triplet), ''.join(reversed(triplet))]:
                    if len(word) >= 4 and is_palindrome(word):
                        palindromes.add(word)
    return palindromes