def palindromes_between_indices(s):
    letters = set(s[5:8].lower()) & set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    if len(letters) > 0:
        if len(letters) == 1:
            palindrome = ''.join(sorted(list(letters))) * 3
            palindromes.add(palindrome)
        else:
            for letter in letters:
                remaining_letters = letters - {letter}
                for r_letter in remaining_letters:
                    palindrome = letter + r_letter + letter
                    palindromes.add(palindrome)
    return palindromes