def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[4:7].lower()
    letter_count = {letter: substring.count(letter) for letter in set(substring) if letter in english_letters}
    for letter, count in letter_count.items():
        if count >= 2:
            palindromes.add(letter * 2)
    for letter1, count1 in letter_count.items():
        for letter2, count2 in letter_count.items():
            if letter1 != letter2 and count1 > 0 and (count2 > 0):
                palindromes.add(letter1 + letter2 + letter1)
    return palindromes