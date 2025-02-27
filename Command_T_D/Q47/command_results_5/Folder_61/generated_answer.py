def palindromes_of_specific_lengths(text):
    palindromes = set()
    for index, character in enumerate(text):
        if character.isalpha():
            length = index + 1
            while length < 31 and length >= 20:
                if text[length].isalpha():
                    length += 1
                else:
                    break
            palindromes.add(character.lower() + text[length:length + length])
    return palindromes