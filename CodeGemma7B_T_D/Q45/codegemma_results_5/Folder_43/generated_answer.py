def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def letter_count(word):
        alphabet = set(word.lower())
        counts = {}
        for letter in alphabet:
            counts[letter] = word.lower().count(letter)
        return counts
    start, end = (2, 5)
    valid_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i + 1, end + 2):
            substring = s[i:j].lower()
            if not substring or substring[-1] not in valid_letters:
                continue
            counts = letter_count(substring)
            if all((count >= 2 for letter, count in counts.items())):
                palindrome = ''.join(sorted(counts.keys(), key=counts.get, reverse=True))
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes