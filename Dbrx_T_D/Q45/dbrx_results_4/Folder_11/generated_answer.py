from collections import defaultdict

def get_letter_frequencies(string):
    letters = defaultdict(int)
    for char in string[3:8].lower():
        if char.isalpha():
            letters[char] += 1
    return letters

def generate_palindromes(letter_frequencies):
    palindromes = set()
    for freq in letter_frequencies.values():
        if freq >= 2:
            palindromes.add(''.join((c * freq for c in 'a' * (freq // 2) + 'b' * (freq % 2))))
            palindromes.add(''.join((c * freq for c in 'b' * (freq // 2) + 'a' * (freq % 2))))
    return palindromes

def palindromes_between_indices(string):
    letters = get_letter_frequencies(string)
    return generate_palindromes(letters)