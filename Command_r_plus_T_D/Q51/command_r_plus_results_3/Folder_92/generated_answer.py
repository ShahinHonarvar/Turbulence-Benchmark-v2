def if_contains_anagrams(lst):
    count = 0
    processed = set()
    for word in lst:
        cleaned_word = ''.join((char for char in word if char.isalpha() and char.lower() in 'abcdefghijklmnopqrstuvwxyz'))
        if len(cleaned_word) < 3:
            continue
        signature = ''.join(sorted(cleaned_word))
        if signature in processed:
            count += 1
        else:
            processed.add(signature)
    return count <= 34