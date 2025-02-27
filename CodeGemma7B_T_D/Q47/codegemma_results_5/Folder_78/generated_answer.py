from nltk.corpus import stopwords
          import re
          from nltk.stem import WordNetLemmatizer

def palindromes_of_specific_lengths(text):
    """
          Returns the set of all palindromes with the specified requirements.
          """
    lem = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = re.sub('[^\\\\w\\\\s]', '', text)
    tokens = re.split('\\\\s+', text)
    lemmatized_tokens = [lem.lemmatize(word) for word in tokens]
    lemmatized_tokens = [word for word in lemmatized_tokens if word not in stop_words]
    text = ' '.join(lemmatized_tokens)
    palindromes = set()
    for i in range(15, 73):
        for j in range(i + 19, i + 56):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes