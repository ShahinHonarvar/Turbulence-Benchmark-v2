from string import ascii_letters

def palindromes_of_specific_lengths(text):
    text = text[39:95].lower()
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(text) - length + 1):
            palindrome = text[i:i + length]
            if palindrome == palindrome[::-1] and all((c in ascii_letters for c in palindrome)):
                palindromes.add(palindrome)
    return palindromes