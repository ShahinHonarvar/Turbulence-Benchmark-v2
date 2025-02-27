from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    substr = s[4:9].lower()
    letter_count = defaultdict(int)
    for letter in substr:
        if letter in english_letters:
            letter_count[letter] += 1
    for c1 in english_letters:
        if letter_count[c1] >= 2:
            for c2 in english_letters:
                if letter_count[c2] >= 1:
                    palindromes.add(c1 + c2 + c1)
    for c1 in english_letters:
        if letter_count[c1] >= 1:
            for c2 in english_letters:
                if letter_count[c2] >= 1:
                    for c3 in english_letters:
                        if letter_count[c3] >= 1:
                            palindromes.add(c1 + c2 + c3 + c2 + c1)
    return palindromes