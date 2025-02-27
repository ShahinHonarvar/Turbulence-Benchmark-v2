def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_letters += english_letters.upper()
    sub_str = s[2:9].lower()
    letter_count = {letter: sub_str.count(letter) for letter in english_letters}
    for letter, count in letter_count.items():
        if count >= 3:
            palindromes.add(letter * count)
    for letter1, count1 in letter_count.items():
        if count1 >= 2:
            for letter2, count2 in letter_count.items():
                if letter1 != letter2 and count2 >= 2:
                    palindromes.add(letter1 * count1 + letter2 * count2)
    for letter1, count1 in letter_count.items():
        if count1 >= 2:
            for letter2, count2 in letter_count.items():
                if letter1 != letter2 and count2 >= 1:
                    for letter3, count3 in letter_count.items():
                        if letter2 != letter3 and count3 >= 1:
                            palindromes.add(letter1 * count1 + letter2 + letter3)
    return {p for p in palindromes if len(p) >= 6 and p == p[::-1]}