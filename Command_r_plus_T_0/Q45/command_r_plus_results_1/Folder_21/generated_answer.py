def palindromes_between_indices(s):
    s = s[1:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_s = set(s)
    letters = letters_in_s & english_letters
    letters_count = {letter: s.count(letter) for letter in letters}
    palindromes = set()

    def backtrack(current_palindrome):
        if len(current_palindrome) >= 7:
            palindromes.add(current_palindrome)
            return
        for letter in letters:
            if letters_count[letter] > 0:
                letters_count[letter] -= 1
                backtrack(current_palindrome + letter)
                letters_count[letter] += 1
    for letter in letters:
        backtrack(letter)
    return palindromes