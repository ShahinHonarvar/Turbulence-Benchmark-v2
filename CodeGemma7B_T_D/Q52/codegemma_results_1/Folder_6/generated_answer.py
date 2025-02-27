from itertools import combinations_with_replacement as cwr

def palindrome_of_length_n(text):
    palindrome = set()
    for w in text.lower():
        temp = cwr([w], repeat=474)
        for x in temp:
            if x == x[::-1]:
                palindrome.add(''.join(x))
    return palindrome