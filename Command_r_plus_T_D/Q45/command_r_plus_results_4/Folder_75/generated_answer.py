def palindromes_between_indices(s):
    sub_str = s[2:5].lower()
    letters = set(filter(str.isalpha, sub_str))
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            palindrome = letter1 + letter2 + letter1
            palindromes.add(palindrome)
    return palindromes