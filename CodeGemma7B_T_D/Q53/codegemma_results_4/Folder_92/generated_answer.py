def palindrome_of_length_at_least_n(text):
    text = text.lower()
    text = text.strip()
    text = text.replace(' ', '')
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace("'", '')
    text = text.replace('"', '')
    text = text.replace(';', '')
    text = text.replace(':', '')
    text = text.replace('/', '')
    text = text.replace('\\\\', '')
    text = text.replace('~', '')
    text = text.replace('@', '')
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j + 1] == text[j:i:-1]:
                if len(text[i:j + 1]) >= 10:
                    palindromes.add(text[i:j + 1])
    return palindromes