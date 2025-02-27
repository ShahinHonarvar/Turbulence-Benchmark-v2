from itertools import product

def palindrome_of_length_at_least_n(text):
    set_of_all_palindromes = set()
    for word in text.lower().split():
        for pos in range(len(word)):
            for length in range(31, len(word) + 1):
                if palindrome_check(word, pos, length):
                    set_of_all_palindromes.add(word[pos:pos + length])
    return set_of_all_palindromes

def palindrome_check(word, pos, length):
    temp = word[pos:pos + length]
    return temp == temp[::-1]