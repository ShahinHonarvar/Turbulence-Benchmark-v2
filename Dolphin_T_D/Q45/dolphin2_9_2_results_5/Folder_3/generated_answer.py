def palindromes_between_indices(s):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    english_letters = set()
    for letter in s[7:10]:
        if letter.lower() in letters:
            english_letters.add(letter.lower())
    palindromes = set()
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            segment = s[i:i + length]
            if set(segment.lower()) <= english_letters and segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes