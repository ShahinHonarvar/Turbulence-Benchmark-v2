from collections import defaultdict

def palindromes_between_indices(input_string):
    input_string = input_string.lower()
    palindromes = set()
    letters_count = {letter: 0 for letter in ENGLISH_LETTERS}
    start_letter_indices = {letter: 0 for letter in ENGLISH_LETTERS}
    end_letter_indices = {letter: 0 for letter in ENGLISH_LETTERS}
    letters_count = defaultdict(int, letters_count)
    start_letter_indices = defaultdict(int, start_letter_indices)
    end_letter_indices = defaultdict(int, end_letter_indices)
    for i in range(len(input_string)):
        if i < 1 or i > 8:
            continue
        letters_count[input_string[i]] += 1
        start_letter_indices[input_string[i]] = max(start_letter_indices[input_string[i]], i)
        end_letter_indices[input_string[i]] = max(end_letter_indices[input_string[i]], i)
    for letter, count in letters_count.items():
        if count < 2:
            continue
        for start in range(start_letter_indices[letter], end_letter_indices[letter] + 1):
            for end in range(end_letter_indices[letter], start - 1, -1):
                if end - start + 1 < 4:
                    continue
                if input_string[start - 1] == input_string[end - 1]:
                    palindrome = input_string[start - 1:end]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes