from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[2:6].lower()
    possible_letters = set(s) & english_letters
    palindromes = set()
    if len(possible_letters) < 2:
        return palindromes
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            current_substr = s[i:i + length]
            if current_substr == current_substr[::-1] and set(current_substr) <= possible_letters:
                palindromes.add(current_substr)
    return palindromes