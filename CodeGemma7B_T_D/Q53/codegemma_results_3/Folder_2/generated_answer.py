from string import ascii_lowercase

def palindrome_of_length_at_least_n(str):
    all_palindromes = set()
    for start in range(len(str) - 4):
        for end in range(start + 5, len(str) + 1):
            sliced_str = str[start:end]
            reversed_str = sliced_str[::-1]
            if sliced_str.lower() == reversed_str.lower():
                all_palindromes.add(sliced_str)
    return all_palindromes