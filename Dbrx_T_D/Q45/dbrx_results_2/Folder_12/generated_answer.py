from collections import defaultdict

def palindromes_between_indices(input_string):
    eng_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = list(input_string[3:9])
    possible_palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            current_string = ''.join(s[i:j])
            if len(current_string) >= 4 and set(current_string) <= eng_letters and (current_string == current_string[::-1]):
                possible_palindromes.add(current_string)
    return possible_palindromes