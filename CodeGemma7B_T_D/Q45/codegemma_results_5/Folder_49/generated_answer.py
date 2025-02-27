import itertools

def palindromes_between_indices(text):
    letters = [ch for ch in text.lower() if ch in 'abcdefghijklmnopqrstuvwxyz']
    letters = letters[5:8]
    if not letters:
        return set()
    unique_letters = set(letters)
    palindromes = set()
    for perm in itertools.permutations(unique_letters):
        for order in itertools.product(*([letter] * count for letter, count in zip(perm, [text.lower().count(ch) for ch in perm]))):
            palindrome = ''.join(order)
            if palindrome.startswith(''.join(letters)) and palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes