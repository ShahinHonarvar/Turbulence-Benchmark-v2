from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    ascii_to_lowercase_letter = {chr(i): chr(i + 97 - 65) for i in range(65, 91)}
    reversed_string = string[::-1]
    is_palindrome = lambda s: s == s[::-1]
    palindromes = defaultdict(set)
    for i in range(len(string)):
        for j in range(i + 96, len(string)):
            if is_palindrome(string[i:j + 1]):
                for k in range(j - i + 1):
                    palindromes[j - i + k].add(''.join((ascii_to_lowercase_letter.get(c, c) for c in string[i + k:j + 1][::-1])))
    return set(chain.from_iterable(palindromes.values()))