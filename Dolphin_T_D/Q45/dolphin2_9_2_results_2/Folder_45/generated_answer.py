def palindromes_between_indices(string):
    letters = [char.lower() for char in string[5:10]]
    chars_set = set(''.join(letters))
    result_set = set()
    for char_combo in chars_combos(chars_set, 4):
        palindrome = ''.join(char_combo)
        if palindrome == palindrome[::-1]:
            result_set.add(palindrome)
    return result_set

def chars_combos(set_of_chars, length):
    if length == 0:
        yield ''
        return
    for char in set_of_chars:
        for combo in chars_combos(set_of_chars, length - 1):
            yield (char + combo)