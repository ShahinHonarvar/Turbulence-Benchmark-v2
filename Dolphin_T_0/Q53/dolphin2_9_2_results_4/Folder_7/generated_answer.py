from re import findall

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for length in range(122, 0, -1):
        for term in findall('[a-z]{%s}' % length, text):
            if term == term[::-1]:
                palindromes.add(term)
    return palindromes