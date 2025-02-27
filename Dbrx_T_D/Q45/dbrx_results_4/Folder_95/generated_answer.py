from collections import defaultdict, Counter

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[7:9].lower()
    possible_letters = eng_letters & set(substr)
    if len(possible_letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for letters in possible_letters:
            if len(letters) < length:
                continue
            for arrangement in permutations(letters, length):
                arrangement = ''.join(arrangement)
                if is_palindrome(arrangement):
                    palindromes.add(arrangement)
    return palindromes