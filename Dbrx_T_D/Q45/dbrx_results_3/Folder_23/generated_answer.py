def palindromes_between_indices(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for start_index in range(len(input_string)):
        for end_index in range(start_index, len(input_string)):
            if end_index - start_index < 3:
                continue
            substring = input_string[start_index:end_index + 1].lower()
            if set(substring) <= english_letters:
                palindrome = ''.join(sorted(substring))
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes