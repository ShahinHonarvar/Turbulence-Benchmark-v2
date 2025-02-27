from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = {letter for letter in s[4:7] if letter.lower() in english_letters}
    palindromes = set()
    for arrangement in permutations(letters_in_range, len(letters_in_range)):
        palindrome = ''.join(arrangement)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes