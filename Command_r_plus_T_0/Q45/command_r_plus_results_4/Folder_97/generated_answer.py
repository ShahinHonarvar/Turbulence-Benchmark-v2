def palindromes_between_indices(s):
    s = s[:5].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(s) & english_letters
    letter_count = {letter: s.count(letter) for letter in letters}
    palindromes = set()
    for letter, count in letter_count.items():
        if count >= 2:
            palindromes.add(letter * 2)
    for letter1, count1 in letter_count.items():
        for letter2 in [l for l in letters if l != letter1 and letter_count[l] >= 1]:
            if count1 >= 1:
                palindromes.add(letter1 + letter2 + letter1)
    return palindromes