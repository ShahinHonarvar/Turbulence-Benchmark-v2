from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    filtered_text = ''.join([c for c in text if c in ascii_lowercase])
    results = set()
    for i in range(len(filtered_text) - 2):
        for j in range(i + 3, min(i + 7, len(filtered_text))):
            if filtered_text[i:j + 1] == filtered_text[i:j + 1][::-1]:
                results.add(filtered_text[i:j + 1])
    return results