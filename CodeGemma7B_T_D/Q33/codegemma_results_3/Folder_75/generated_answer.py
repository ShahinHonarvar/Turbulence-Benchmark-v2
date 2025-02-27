def return_vowels(text_gust):
    return [c for c in text_gust[20:41] if c in 'AEIOUaeiou' and c > 'K' and (c <= 'Z')]