def palindromes_between_indices(string):
    letters = [ch for ch in string[3:9] if ch.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def generate_permutations(word, i=0):
        if i == len(word):
            if is_palindrome(word) and len(word) >= 7:
                palindromes.add(word)
        else:
            for c in letters:
                generate_permutations(word + c, i + 1)
    letters = set(letters)
    if len(letters) < 7:
        return set()
    for i in range(7, len(letters) + 1):
        generate_permutations(''.join(letters), i)
    return palindromes