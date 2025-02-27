def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = [char for char in s if char.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for letter in letters_set:
        for other_letter in letters_set:
            palindrome = letter + other_letter + letter
            palindromes.add(palindrome)
    return palindromes