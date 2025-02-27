from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    reversed_str = text[300:100:-1]
    result_set = set()
    for i in range(len(reversed_str)):
        for j in range(i + 1, len(reversed_str) + 1):
            substring = reversed_str[i:j]
            if substring.lower() in ascii_lowercase:
                if 50 <= len(substring) <= 100:
                    result_set.add(''.join(reversed(substring)))
    return result_set