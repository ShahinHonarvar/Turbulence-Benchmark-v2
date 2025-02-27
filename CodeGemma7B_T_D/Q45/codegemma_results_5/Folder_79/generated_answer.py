def palindromes_between_indices(text):
    palindromes = set()
    for child in text[1:8]:
        for parent in text[text.index(child):]:
            if parent in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and child.lower() == parent.lower():
                palindromes.add(parent + child + parent)
    return palindromes